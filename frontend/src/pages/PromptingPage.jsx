import { useState } from 'react';
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
     /**
      * Call to the backend API to submit the form data
      */
    } catch (err) {
      console.error(err);
     
    }
  };

  return (
    <div className="mt-8 mx-auto max-w-md p-8 rounded-lg bg-[#2C2C2C] shadow-md shadow-red-500/50">
    <h2 className="text-2xl font-bold text-gray-100 mb-6">Get a Reccomendation!</h2>
      <form onSubmit={handleSubmit} className="space-y-4">
        <div className="flex flex-col">
          <label htmlFor="user_id" className="mb-1 text-sm font-medium text-gray-100">
            User ID
          </label>
          <input
            type="number"
            id="user_id"
            name="user_id"
            value={formData.user_id}
            required
            className="border border-gray-300 rounded px-3 py-2 bg-gray-50"
          />
        </div>

        {/* Name, Email */}
        <div className="flex flex-col">
          <label htmlFor="name" className="mb-1 text-sm font-medium text-gray-100">Name</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formData.name}
            required
            className="border border-gray-300 rounded px-3 py-2 bg-gray-50"
          />
        </div>
        <div className="flex flex-col">
          <label htmlFor="email" className="mb-1 text-sm font-medium text-gray-100">Email</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            required
            className="border border-gray-300 rounded px-3 py-2 bg-gray-50"
          />
        </div>

        {/* Numeric fields */}
        {['age','bmi','height','weight'].map((field) => (
          <div key={field} className="flex flex-col">
            <label htmlFor={field} className="mb-1 text-sm font-medium text-gray-100">
              {field.charAt(0).toUpperCase() + field.slice(1)}
            </label>
            <input
              type="number"
              step={field==='age'? '1' : 'any'}
              id={field}
              name={field}
              value={formData[field]}
              required
              className="border border-gray-300 rounded px-3 py-2 bg-gray-50"
            />
          </div>
        ))}

        {/* Boolean fields as groups */}
        {[
          { name: 'diabetes', label: 'Do you have diabetes?' },
          { name: 'overweight', label: 'Are you overweight?' },
          { name: 'heart_disease', label: 'History of heart disease?' },
          { name: 'smoking', label: 'Do you smoke?' },
          { name: 'alcohol', label: 'Do you consume alcohol?' },
        ].map(({ name, label }) => (
          <fieldset key={name} className="flex flex-col">
            <legend className="mb-1 text-sm font-medium text-gray-100">{label}</legend>
            <div className="flex space-x-4">
              {['true','false'].map((val) => (
                <label key={val} className="inline-flex items-center space-x-2">
                  <input
                    type="radio"
                    name={name}
                    value={val}
                    checked={formData[name] === val}
                    required
                    className="form-radio"
                  />
                  <span className="text-gray-100">{val === 'true' ? 'Yes' : 'No'}</span>
                </label>
              ))}
            </div>
          </fieldset>
        ))}

        {/* Family history */}
        <div className="flex flex-col">
          <label htmlFor="family_history" className="mb-1 text-sm font-medium text-gray-100">
            Family Medical History
          </label>
          <textarea
            id="family_history"
            name="family_history"
            value={formData.family_history}
            required
            className="border border-gray-300 rounded px-3 py-2 bg-gray-50"
            rows={3}
          />
        </div>

        {/* Question */}
        <div className="flex flex-col">
          <label htmlFor="question" className="mb-1 text-sm font-medium text-gray-100">Your Question</label>
          <textarea
            id="question"
            name="question"
            value={formData.question}
            required
            className="border border-gray-300 rounded px-3 py-2 bg-gray-50"
            rows={4}
          />
        </div>

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
