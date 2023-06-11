import logo from './logo.svg';
import './App.css';
import Dropdown from './components/Dropdown';
import { useState } from 'react';


const dropDown = [
  {
    btnTit : '1',
    link: '/main',
    listItems : [ 'item 1', 'item 2', 'item 3' ]
  },
  {
    btnTit : '2',
    link: '/hello',
    listItems : [ 'item 1', 'item 2' ]
  }
]

function App() {
  
  return (
    <nav className="App" style={{ display: 'flex', columnGap: '5rem', width: '100vw', height: '3.5em', backgroundColor: 'grey'}}>
      { dropDown.map((dd, idx) => <Dropdown key={idx} btnTit={dd.btnTit} link={dd.link} listItems={dd.listItems} />)}
    </nav>
  );
}

export default App;
