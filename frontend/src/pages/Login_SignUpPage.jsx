import { Link } from "react-router-dom"

import api from '../api'
import { useState } from 'react';
import { Loading } from "../components/Loading";

export default function LoginPage() {

    // Variables and setters for userId and pass word
    const [userId, setUserId] = useState('');
    const [password, setPassword] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    const handleLogin = async (e) => {
        e.preventDefault();

        const payload = {
            user_id : Number(userId),
            password : password
        }

        try {
            setIsLoading(true);
            const response = await api.post('/login', payload)
            localStorage.setItem("token", response.data.access_token);
            alert('Login Sucessful')
        }
        
        catch (err) {
            console.error(err);
            alert("Error, incorrect login credentials");
        }
        
        finally {
            setIsLoading(false);
        }
        
    };

    return (
        <div className="flex items-center justify-center min-h-screen p-4">
         <div className="w-full sm:w-2/3 md:w-1/2 lg:w-1/3 p-8 rounded-lg bg-[#2C2C2C] shadow-lg">
            <h2 className="text-2xl font-bold text-gray-100 mb-6">Login</h2>
            <form onSubmit={handleLogin}>
                <div className="mb-8">
                    <label htmlFor="username" className="block text-gray-300 mb-2">User Id</label>
                    <input type="text" id="user_ud" name="user_id" onChange={(e) => setUserId(e.target.value)} className="w-full p-2 rounded bg-gray-950 text-gray-100" placeholder="Enter your user ID" />
                </div>
                <div className="mb-8">
                    <label htmlFor="password" className="block text-gray-300 mb-2">Password</label>
                    <input type="password" id="password" name="password" onChange={(e) => setPassword(e.target.value)} className="w-full p-2 rounded bg-gray-950 text-gray-100" placeholder="Enter your password" />
                </div>
                <button type="submit" className="w-full bg-red-600 hover:bg-red-800 transition-colors duration-200 text-white font-bold py-2 px-4 rounded cursor-pointer">
                    Login
                    </button>
                <p className="mt-4 text-gray-400 text-sm">Don't have an account? <Link to="/signup" className="text-red-500 hover:underline">Sign Up</Link></p>
            </form>

            </div>
            {isLoading && (<Loading />)}
        </div>
    )
};