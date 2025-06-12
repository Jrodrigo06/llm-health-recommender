export function FormField({ label, id, children }) {
  return (
    <div className="flex flex-col">
      <label htmlFor={id} className="mb-1 text-sm font-medium text-gray-100">
        {label}
      </label>
      {children}
    </div>
  );
}