export default function AboutPage() {
    return (
        <div> 
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mt-8">
            <div className="mx-4 p-8 rounded-lg bg-[#2C2C2C] shadow-[0_0_20px_0_rgba(255,0,0,0.5)]"> 
                <h2 className="text-2xl font-bold text-gray-100 mb-6">About Us</h2>
                <p className="text-gray-300">
                    Welcome to our nutrition recommendation platform! We are dedicated to providing personalized nutrition advice based on your unique needs and preferences.
                </p>
            </div>
        </div>
        </div>
    );
}