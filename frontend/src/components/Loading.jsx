export function Loading(){
    return(
        <div className="fixed inset-0 z-50 flex flex-col items-center justify-center bg-black/60">
         <div className="w-16 h-16 border-4 border-t-transparent border-white rounded-full animate-spin" />
          <h1 className="mt-4 text-white">Loading…</h1>
        </div>
    )
}
