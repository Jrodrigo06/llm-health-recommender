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

  
const textFields = [
  { id: 'user_id', label: 'User Id', type: 'number', placeholder: '123' },
  { id: 'name',  label: 'Name', type: 'text', placeholder: 'Jane Doe' },
  { id: 'email', type: 'email', placeholder: 'jane@example.com' },
  { id: 'age', label: 'Age', type: 'number', placeholder: '30' },
  { id: 'bmi', label: 'BMI', type: 'number', placeholder: '22.5' },
  { id: 'height', label: 'Height', type: 'number', placeholder: '170' },
  { id: 'weight', label: 'Weight', type: 'number', placeholder: '65' },
];

const textAreas = [
  { id: 'family_history', label:'Provide any family history', rows: 3, placeholder: 'E.g. heart disease in father' },
  { id: 'question', label: 'Question', rows: 4, placeholder: 'Your question…' },
];

const booleanFields = [
  { id: 'diabetes', label: 'Do you have diabetes?' },
  { id: 'overweight', label: 'Are you overweight?' },
  { id: 'heart_disease', label: 'History of heart disease?' },
  { id: 'smoking', label: 'Do you smoke?' },
  { id: 'alcohol', label: 'Do you consume alcohol?' },
];

  return (
    <div className="mt-8 mb-8 mx-auto max-w-md p-8 rounded-lg bg-[#2C2C2C] shadow-[0_0_20px_0_rgba(255,0,0,0.5)]">
    <h2 className="text-2xl font-bold text-gray-100 mb-6">Get a Recommendation!</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
         {textFields.map(f => (
            <TextInput
            key={f.id}
            id={f.id}
            name={f.id}
            label = {f.label}
            type={f.type}
            placeholder={f.placeholder}
            value={formData[f.id]}
            onChange={handleChange}
            />
        ))}

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

        {booleanFields.map(f => (
            <RadioGroup
            key={f.id}
            id={f.id}
            name={f.id}
            value={formData[f.id]}
            label = {f.label}
            onChange={handleChange}
            options={[
                { value: 'true', label: 'Yes' },
                { value: 'false', label: 'No' },
            ]}
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
