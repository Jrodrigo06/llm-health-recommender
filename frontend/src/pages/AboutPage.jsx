export default function AboutPage() {
    return (
        <div> 
        <div className="grid grid-cols-1 md:grid-cols-2 gap-20 mt-8 mx-auto max-w-7xl">
            <div className="w-full md:w-5/6 lg:w-4/5 mx-auto p-8 rounded-lg bg-[#2C2C2C] shadow-[0_0_10px_0_rgba(255,0,0,0.2)]"> 
                <h2 className="text-2xl font-bold text-gray-100 mb-6">About this project</h2>
                <h3 className="text-xl font-semibold text-gray-200 mb-4">Overview</h3>
                <p className="text-gray-300 mb-5 leading-relaxed">
                    This project is a web application designed to provide personalized nutrition recommendations based on user input. It helps users get tailored advice quickly and conveniently through an intuitive web interface.
                </p>

                <h3 className="text-xl font-semibold text-gray-200 mb-4">How it Works</h3>
                <p className="text-gray-300 mb-5 leading-relaxed">
                    The app uses a Retrieval-Augmented Generation (RAG) pipeline with sourced health documents to analyze user questions and generate responses. It features user authentication with JWT, allowing users to securely log in, access their history of recommendations, and receive appropriate error messages when not logged in.
                </p>

                <p className="text-gray-300 mb-5 leading-relaxed">
                    The application is built with React for the frontend, FastAPI for the backend, ChromaDB for the vector database, Llama 2 for the llm, MongoDB for data storage.
                </p>
            </div>
            <div className="w-full md:w-5/6 lg:w-4/5 mx-auto p-8 rounded-lg bg-[#2C2C2C] shadow-[0_0_10px_0_rgba(255,0,0,0.2)]"> 
                <h2 className="text-2xl font-bold text-gray-100 mb-6">Why I made this project</h2>
                <p className="text-gray-300 mb-5 leading-relaxed">
                    I created this project to experiment with Retrieval-Augmented Generation (RAG). Health advice is an area where RAG effectively addresses the limitations of using LLMs alone, improving accuracy and relevance in the responses.
                </p>
                <p className="text-gray-300 mb-5 leading-relaxed">
                    For example, a regular LLM might generate a response it's not sure about, or pull inaccurate information from its training data. In contrast, a RAG system can retrieve specific, up-to-date information from trusted sources, ensuring that the advice given is both accurate and relevant to the user's query.
                </p>
                <p className="text-gray-300 mb-5 leading-relaxed"> 
                    I also made this as I am intrested in different intersections in data science like data science and healthcare, and I wanted to create a project that combines these two fields. 
                </p>

                <p className="text-gray-300 mb-5 leading-relaxed">
                    In the future, I hope to expand on this project by adding more features, or implementing a new AI system and possibly deploy it into the cloud.
                </p>


       
            </div>
        </div>
        </div>
    );
}