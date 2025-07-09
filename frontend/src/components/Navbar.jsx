import React from 'react';
import styles from './Navbar.module.css';
//import styles from '../App.css';
//import styles from '../index.css';

function Navbar() {
    return (<nav className = {styles['navbar']}>

        <a href="/" className = {styles['site-title']}>Nutrition Recommender</a>
        <ul>
            <li> <a href="/about">About</a> </li>
            <li> <a href="/ask">Ask a question!</a> </li>
            <li> <a href="/history">Get History</a> </li>
            <li> <a href="/login">Login / Sign Up</a> </li>
            
        </ul>
        

    </nav>);

}

export default Navbar;