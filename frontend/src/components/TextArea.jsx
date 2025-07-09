import { FormField } from './FormField';

export function TextArea({ id, name, label, value, onChange, rows = 3, placeholder }) {
  return (
    <FormField label={label} id={id}>
      <textarea
        id={id}
        name={name}
        value={value}
        onChange={onChange}
        rows={rows}
        placeholder={placeholder}
        required
        className="border border-gray-300 rounded px-3 py-2 bg-gray-50 text-black"
      />
    </FormField>
  );
}
