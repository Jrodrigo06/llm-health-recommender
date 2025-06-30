export function Loading() {
  return (
    <div className="fixed inset-0 z-50 flex flex-col items-center justify-center bg-black/60">
      <div
        className="
          w-8 h-8 bg-white rounded-full
          animate-bounce
          ease-in-out
          duration-1000
        "
      />
      <h1 className="mt-4 text-white">Loading…</h1>
    </div>
  )
}
