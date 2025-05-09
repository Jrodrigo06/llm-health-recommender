import React from 'react';
import { useState } from 'react';   

function Navbar() {
    return (<nav className = "navbar">

        <a href="/" className = "site-title">Health Recommender</a>
        <ul>
            <li> <a href="/about">About</a> </li>
            <li> <a href="/ask">Ask a question!</a> </li>
        </ul>
        

    </nav>);

}

export default Navbar;