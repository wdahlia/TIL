import React, { useState } from 'react';
import { Link } from 'react-router-dom';

export default function Dropdown({ ...props }) {

  const { btnTit, link, listItems } = props

  const [ open, setOpen ]= useState(false);

  const handleMouseOver = () => setOpen(true)

  const handleMouseOut = () => setOpen(false)

  return (
    <ul onMouseOver={handleMouseOver} onMouseOut={handleMouseOut} onClick={() => console.log('클릭!')} style={{ width: '100px', minHeight: '100px', listStyle: 'none' }}>
      { btnTit }
      <div style={{ position: 'relative', height: '100%', top: '50px', left: '5px' }}>{ open ? listItems.map((item, idx) => <li key={idx} style={{ margin: '1rem 0' }} onClick={() => console.log('클릭!')}>{item}</li>) : null }</div>
    </ul>
  );
}

