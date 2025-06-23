import { Loading } from "../components/Loading";
import { useState } from "react";
import api from "../api";

export default function GetHistoryPage() {

    const [isLoading, setIsLoading] = useState(false);

    const handleGetHistory = async () => {
        try {
            const response = await api.get('/history');
            setIsLoading(true);
            console.log(response.data);
            alert('History retrieved successfully!');
        } catch (error) {
            console.error('Error fetching history:', error);
            alert('Failed to retrieve history.');
        }
        finally {
            setIsLoading(false);
        }
    };

    return (
        <div>
            <div className="mt-8 mb-8 mx-auto max-w-md p-8 rounded-lg bg-[#2C2C2C] shadow-[0_0_20px_0_rgba(255,0,0,0.5)]">
            <h1 className="text-2xl font-bold text-gray-100 mb-6">Get History</h1>
            <p>Get the history of your nutrition recommendations.</p>
            <button 
                onClick={handleGetHistory} 
                className="w-full py-2 mt-4 font-semibold text-white bg-red-500 rounded hover:bg-red-600 transition-colors duration-200"> 
                Get History
            </button>
            </div>
            {isLoading && <Loading />}
        </div>
    );
}