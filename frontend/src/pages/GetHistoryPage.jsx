export default function GetHistoryPage() {

    return (
        <div>
            <div className="mt-8 mb-8 mx-auto max-w-md p-8 rounded-lg bg-[#2C2C2C] shadow-[0_0_20px_0_rgba(255,0,0,0.5)]">
            <h1 className="text-2xl font-bold text-gray-100 mb-6">Get History</h1>
            <p>Get the history of your nutrition recommendations.</p>
            <button className="w-full py-2 mt-4 font-semibold text-white bg-red-500 rounded hover:bg-red-600 transition-colors duration-200"> 
                Get History
            </button>
            </div>
        </div>
    );
}