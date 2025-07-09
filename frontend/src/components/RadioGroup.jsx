import { FormField } from './FormField';

export function RadioGroup({ id, name, label, value, onChange, options }) {
  return (
    <FormField label={label} id={id}>
      <div className="flex space-x-4">
        {options.map(opt => (
          <label key={opt.value} className="inline-flex items-center space-x-2">
            <input
              type="radio"
              id={`${id}-${opt.value}`}
              name={name}
              value={opt.value}
              checked={value === opt.value}
              onChange={onChange}
              required
              className="form-radio"
            />
            <span className="text-gray-100">{opt.label}</span>
          </label>
        ))}
      </div>
    </FormField>
  );
}