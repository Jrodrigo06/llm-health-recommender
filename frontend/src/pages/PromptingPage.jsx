import { useEffect, useState } from 'react';
import { TextArea } from '../components/TextArea';
import api from '../api';
import { Loading } from '../components/Loading';


export default function UserRequestForm() {
  

  const [question, setQuestion] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [recommendation, setRecommendation] = useState('');

  // 1) On mount, check token validity
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



  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      question: question
    };

    try {
      console.log(payload)
      setIsLoading(true);
      const response = await api.post('/predict', payload)
      setRecommendation(response.data.recommendation);
      console.log(response.data.recommendation);
      alert('Recommendation submitted successfully!');
    } catch (err) {
      console.error(err);
     
    } finally {
      setIsLoading(false);
    }

  };

  


const textAreas = [
  { id: 'question', label: 'Question', rows: 4, placeholder: 'Your question…' },
];


  return (
    <div> 
    <div className="mt-8 mb-8 mx-auto max-w-md p-8 rounded-lg bg-[#2C2C2C] shadow-[0_0_20px_0_rgba(255,0,0,0.5)]">
    <h2 className="text-2xl font-bold text-gray-100 mb-6">Get a Recommendation!</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
         {textAreas.map(f => (
            <TextArea
            key={f.id}
            id={f.id}
            name={f.id}
            label={f.label}
            rows={f.rows}
            placeholder={f.placeholder}
            onChange={(e) => setQuestion(e.target.value)}
            />
        ))}

        <button
          type="submit"
          className="w-full py-2 mt-4 font-semibold text-white bg-red-500 rounded hover:bg-red-600 transition-colors duration-200"
        >
          Submit
        </button>
      </form>
    </div>
    {isLoading && (<Loading />)}

    {recommendation !== '' && (
      <div className="mt-8 mb-8 mx-auto max-w-md p-8 rounded-lg bg-[#2C2C2C] shadow-[0_0_20px_0_rgba(255,0,0,0.5)]"> 
         <h2 className="text-2xl font-bold text-gray-100 mb-6">Recommendation</h2>
         <p className="text-gray-200 whitespace-pre-line">
              {recommendation}
         </p>
      </div>
       )}      
    </div>
  );
}
