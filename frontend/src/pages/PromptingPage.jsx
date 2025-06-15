import { useState } from 'react';
import { TextInput } from '../components/TextInput';
import { TextArea } from '../components/TextArea';
import { RadioGroup } from '../components/RadioGroup';
import api from '../api';

export default function UserRequestForm() {
  const [formData, setFormData] = useState({
    user_id: '',
    name: '',
    email: '',
    age: '',
    bmi: '',
    height: '',
    weight: '',
    diabetes: '',
    overweight: '',
    heart_disease: '',
    family_history: '',
    smoking: '',
    alcohol: '',
    question: ''
  });

    const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };


  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      user_id: Number(formData.user_id),
      user_info: {
        name: formData.name,
        email: formData.email,
        age: Number(formData.age),
        bmi: parseFloat(formData.bmi),
        height: parseFloat(formData.height),
        weight: parseFloat(formData.weight),
        diabetes: formData.diabetes === 'true',
        overweight: formData.overweight === 'true',
        heart_disease: formData.heart_disease === 'true',
        family_history: formData.family_history,
        smoking: formData.smoking === 'true',
        alcohol: formData.alcohol === 'true',
      },
      question: formData.question
    };

    try {
     const response = await api.post('/predict', payload)
     console.log('Response:', response.data);
     alert('Recommendation submitted successfully!');
    } catch (err) {
      console.error(err);
     
    }
  };

  


const textAreas = [
  { id: 'question', label: 'Question', rows: 4, placeholder: 'Your question…' },
];


  return (
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
            value={formData[f.id]}
            onChange={handleChange}
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
  );
}
