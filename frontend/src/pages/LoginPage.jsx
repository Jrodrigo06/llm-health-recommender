import styles from './LoginPage.module.css';
import React from 'react';


export default function LoginPage() {
    return (
        <div className={styles['login-page']}>
            <div className={styles['form-container']}>
            <h1 className={styles['header']}>Login Page</h1>
            <form>
                <label>
                    id:
                    <input type="text" name="username" />
                </label>
                <br />
                <label>
                    Password:
                    <input type="password" name="password" />
                </label>
                <br />
                <button type="submit">Login</button>
            </form>
            </div>
        </div>

    );
}