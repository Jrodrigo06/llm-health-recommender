import { FormField } from './FormField';

export function TextInput({ id, name, value, label, onChange, type = 'text', placeholder }) {
  return (
    <FormField label={label} id={id}>
      <input
        type={type}
        id={id}
        name={name}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        required
        className="border border-gray-300 rounded px-3 py-2 bg-gray-50 text-black"
      />
    </FormField>
  );
}
