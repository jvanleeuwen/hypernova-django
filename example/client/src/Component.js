import React from 'react';
import { renderReact } from 'hypernova-react';

const Component = ({ prop }) => (
  <div>
    {prop}
  </div>
);

export default renderReact('Component.js', Component);
