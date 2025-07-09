import { Loading } from "../components/Loading";
import { useState, useEffect } from "react";
import api from "../api";

export default function GetHistoryPage() {

    const [isLoading, setIsLoading] = useState(false);
    const [history, setHistory] = useState([]);

    useEffect(() => {
    const checkToken = async () => {
      try {
        await api.get('/validate_token');
      } catch {
        localStorage.removeItem('token');
        window.location.replace('/login');
        alert('Your session has expired. Please log in.');
      }
    };
    checkToken();
  }, []);


    const handleGetHistory = async () => {
        try {
            const response = await api.get('/history');
            setHistory(response.data.history || []); 
            setIsLoading(true);
            console.log(response.data);
            alert('History retrieved successfully!');
        } catch (error) {
            console.error('Error fetching history:', error);
            alert('Failed to retrieve history.');
        }
        finally {
          setIsLoading(false);
          console.log(response.data.history);
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
              <div className="mt-6">
                {history.length > 0 ? (
                    <ul className="space-y-4">
                        {history.map((item, index) => (
                            <li key={index} className="p-4 bg-[#3A3A3A] rounded-2xl shadow">
                                <h3 className="text-lg font-bold text-white">{item.question}</h3>
                                <h2 className="text-md font-style: italic mt-2 text-white">Reponse from coach:</h2>
                                <p className="text-gray-300 mt-2">{item.response.recommendation}</p>
                            </li>
                        ))}
                    </ul>
                ) : (
                    <p className="text-gray-400">No history available or not loaded</p>
                )}

              </div>
            </div>
            {isLoading && <Loading />}
        </div>
    );
}