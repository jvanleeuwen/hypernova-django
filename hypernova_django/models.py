# -*- coding: utf-8 -*-
import json
import re
import requests


def reducer(obj, init, f):
    return reduce(lambda a, b: f(a, b), obj.keys(), init)


def encode(obj):
    return re.sub(r'/-->/g', '--&gt;', json.dumps(obj))


def render_html(view_name, data):
    data = encode(data)
    return (
        "<div data-hypernova-key=\"{view_name}\"></div>"
        "<script type=\"application/json\" data-hypernova-key=\"{view_name}\"><!--${data}--></script>"
    ).format(view_name=view_name, data=data)


class Renderer(object):

    def __init__(self, options):
        super(Renderer, self).__init__()

        self.url = options.get('url')
        self.plugins = options.get('plugins', [])
        self.config = {
            'timeout': 1000,
            'headers': {'Content-Type': 'application/json'},
        }
        self.config.update(options)

    def add_plugin(self, plugin):
        self.plugins.append(plugin)

    def plugin_reduce(self, event_name, f, initial):
        def reducer(res, plugin):
            if plugin[event_name]:
                return f(plugin[event_name], res)
            return res

        return reduce(reducer, self.plugins, initial)

    def prepare_request(self, jobs):

        def plugin(plugin, next):
            return plugin(next, jobs)

        jobsHash = self.plugin_reduce(
            'prepareRequest',
            plugin,
            jobs
        )

        print jobsHash

        return {
            'shouldSendRequest': True,
            'jobsHash': jobsHash,
        }

    def create_jobs(self, jobs):

        def func(obj, name):
            data = jobs[name]

            def resolve_plugin(plugin, new_data):
                return plugin(name, new_data)

            try:
                data = self.plugin_reduce(
                    'getViewData',
                    resolve_plugin,
                    jobs[name]
                )
            except:
                pass

            obj[name] = {
                'name': name,
                'data': data,
            }

            return obj

        return reducer(jobs, {}, func)

    def render(self, data):
        jobs = self.create_jobs(data)
        prepared = self.prepare_request(jobs)

        print prepared['jobsHash']

        result = requests.post(self.url, json=prepared['jobsHash'], headers=self.config['headers'])

        return result.text
