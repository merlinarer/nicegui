from typing import Literal

GradientColorStops = Literal[
    'from-inherit',
    'from-current',
    'from-transparent',
    'from-black',
    'from-white',
    'from-slate-50',
    'from-slate-100',
    'from-slate-200',
    'from-slate-300',
    'from-slate-400',
    'from-slate-500',
    'from-slate-600',
    'from-slate-700',
    'from-slate-800',
    'from-slate-900',
    'from-slate-950',
    'from-gray-50',
    'from-gray-100',
    'from-gray-200',
    'from-gray-300',
    'from-gray-400',
    'from-gray-500',
    'from-gray-600',
    'from-gray-700',
    'from-gray-800',
    'from-gray-900',
    'from-gray-950',
    'from-zinc-50',
    'from-zinc-100',
    'from-zinc-200',
    'from-zinc-300',
    'from-zinc-400',
    'from-zinc-500',
    'from-zinc-600',
    'from-zinc-700',
    'from-zinc-800',
    'from-zinc-900',
    'from-zinc-950',
    'from-neutral-50',
    'from-neutral-100',
    'from-neutral-200',
    'from-neutral-300',
    'from-neutral-400',
    'from-neutral-500',
    'from-neutral-600',
    'from-neutral-700',
    'from-neutral-800',
    'from-neutral-900',
    'from-neutral-950',
    'from-stone-50',
    'from-stone-100',
    'from-stone-200',
    'from-stone-300',
    'from-stone-400',
    'from-stone-500',
    'from-stone-600',
    'from-stone-700',
    'from-stone-800',
    'from-stone-900',
    'from-stone-950',
    'from-red-50',
    'from-red-100',
    'from-red-200',
    'from-red-300',
    'from-red-400',
    'from-red-500',
    'from-red-600',
    'from-red-700',
    'from-red-800',
    'from-red-900',
    'from-red-950',
    'from-orange-50',
    'from-orange-100',
    'from-orange-200',
    'from-orange-300',
    'from-orange-400',
    'from-orange-500',
    'from-orange-600',
    'from-orange-700',
    'from-orange-800',
    'from-orange-900',
    'from-orange-950',
    'from-amber-50',
    'from-amber-100',
    'from-amber-200',
    'from-amber-300',
    'from-amber-400',
    'from-amber-500',
    'from-amber-600',
    'from-amber-700',
    'from-amber-800',
    'from-amber-900',
    'from-amber-950',
    'from-yellow-50',
    'from-yellow-100',
    'from-yellow-200',
    'from-yellow-300',
    'from-yellow-400',
    'from-yellow-500',
    'from-yellow-600',
    'from-yellow-700',
    'from-yellow-800',
    'from-yellow-900',
    'from-yellow-950',
    'from-lime-50',
    'from-lime-100',
    'from-lime-200',
    'from-lime-300',
    'from-lime-400',
    'from-lime-500',
    'from-lime-600',
    'from-lime-700',
    'from-lime-800',
    'from-lime-900',
    'from-lime-950',
    'from-green-50',
    'from-green-100',
    'from-green-200',
    'from-green-300',
    'from-green-400',
    'from-green-500',
    'from-green-600',
    'from-green-700',
    'from-green-800',
    'from-green-900',
    'from-green-950',
    'from-emerald-50',
    'from-emerald-100',
    'from-emerald-200',
    'from-emerald-300',
    'from-emerald-400',
    'from-emerald-500',
    'from-emerald-600',
    'from-emerald-700',
    'from-emerald-800',
    'from-emerald-900',
    'from-emerald-950',
    'from-teal-50',
    'from-teal-100',
    'from-teal-200',
    'from-teal-300',
    'from-teal-400',
    'from-teal-500',
    'from-teal-600',
    'from-teal-700',
    'from-teal-800',
    'from-teal-900',
    'from-teal-950',
    'from-cyan-50',
    'from-cyan-100',
    'from-cyan-200',
    'from-cyan-300',
    'from-cyan-400',
    'from-cyan-500',
    'from-cyan-600',
    'from-cyan-700',
    'from-cyan-800',
    'from-cyan-900',
    'from-cyan-950',
    'from-sky-50',
    'from-sky-100',
    'from-sky-200',
    'from-sky-300',
    'from-sky-400',
    'from-sky-500',
    'from-sky-600',
    'from-sky-700',
    'from-sky-800',
    'from-sky-900',
    'from-sky-950',
    'from-blue-50',
    'from-blue-100',
    'from-blue-200',
    'from-blue-300',
    'from-blue-400',
    'from-blue-500',
    'from-blue-600',
    'from-blue-700',
    'from-blue-800',
    'from-blue-900',
    'from-blue-950',
    'from-indigo-50',
    'from-indigo-100',
    'from-indigo-200',
    'from-indigo-300',
    'from-indigo-400',
    'from-indigo-500',
    'from-indigo-600',
    'from-indigo-700',
    'from-indigo-800',
    'from-indigo-900',
    'from-indigo-950',
    'from-violet-50',
    'from-violet-100',
    'from-violet-200',
    'from-violet-300',
    'from-violet-400',
    'from-violet-500',
    'from-violet-600',
    'from-violet-700',
    'from-violet-800',
    'from-violet-900',
    'from-violet-950',
    'from-purple-50',
    'from-purple-100',
    'from-purple-200',
    'from-purple-300',
    'from-purple-400',
    'from-purple-500',
    'from-purple-600',
    'from-purple-700',
    'from-purple-800',
    'from-purple-900',
    'from-purple-950',
    'from-fuchsia-50',
    'from-fuchsia-100',
    'from-fuchsia-200',
    'from-fuchsia-300',
    'from-fuchsia-400',
    'from-fuchsia-500',
    'from-fuchsia-600',
    'from-fuchsia-700',
    'from-fuchsia-800',
    'from-fuchsia-900',
    'from-fuchsia-950',
    'from-pink-50',
    'from-pink-100',
    'from-pink-200',
    'from-pink-300',
    'from-pink-400',
    'from-pink-500',
    'from-pink-600',
    'from-pink-700',
    'from-pink-800',
    'from-pink-900',
    'from-pink-950',
    'from-rose-50',
    'from-rose-100',
    'from-rose-200',
    'from-rose-300',
    'from-rose-400',
    'from-rose-500',
    'from-rose-600',
    'from-rose-700',
    'from-rose-800',
    'from-rose-900',
    'from-rose-950',
    'from-0%',
    'from-5%',
    'from-10%',
    'from-15%',
    'from-20%',
    'from-25%',
    'from-30%',
    'from-35%',
    'from-40%',
    'from-45%',
    'from-50%',
    'from-55%',
    'from-60%',
    'from-65%',
    'from-70%',
    'from-75%',
    'from-80%',
    'from-85%',
    'from-90%',
    'from-95%',
    'from-100%',
    'via-inherit',
    'via-current',
    'via-transparent',
    'via-black',
    'via-white',
    'via-slate-50',
    'via-slate-100',
    'via-slate-200',
    'via-slate-300',
    'via-slate-400',
    'via-slate-500',
    'via-slate-600',
    'via-slate-700',
    'via-slate-800',
    'via-slate-900',
    'via-slate-950',
    'via-gray-50',
    'via-gray-100',
    'via-gray-200',
    'via-gray-300',
    'via-gray-400',
    'via-gray-500',
    'via-gray-600',
    'via-gray-700',
    'via-gray-800',
    'via-gray-900',
    'via-gray-950',
    'via-zinc-50',
    'via-zinc-100',
    'via-zinc-200',
    'via-zinc-300',
    'via-zinc-400',
    'via-zinc-500',
    'via-zinc-600',
    'via-zinc-700',
    'via-zinc-800',
    'via-zinc-900',
    'via-zinc-950',
    'via-neutral-50',
    'via-neutral-100',
    'via-neutral-200',
    'via-neutral-300',
    'via-neutral-400',
    'via-neutral-500',
    'via-neutral-600',
    'via-neutral-700',
    'via-neutral-800',
    'via-neutral-900',
    'via-neutral-950',
    'via-stone-50',
    'via-stone-100',
    'via-stone-200',
    'via-stone-300',
    'via-stone-400',
    'via-stone-500',
    'via-stone-600',
    'via-stone-700',
    'via-stone-800',
    'via-stone-900',
    'via-stone-950',
    'via-red-50',
    'via-red-100',
    'via-red-200',
    'via-red-300',
    'via-red-400',
    'via-red-500',
    'via-red-600',
    'via-red-700',
    'via-red-800',
    'via-red-900',
    'via-red-950',
    'via-orange-50',
    'via-orange-100',
    'via-orange-200',
    'via-orange-300',
    'via-orange-400',
    'via-orange-500',
    'via-orange-600',
    'via-orange-700',
    'via-orange-800',
    'via-orange-900',
    'via-orange-950',
    'via-amber-50',
    'via-amber-100',
    'via-amber-200',
    'via-amber-300',
    'via-amber-400',
    'via-amber-500',
    'via-amber-600',
    'via-amber-700',
    'via-amber-800',
    'via-amber-900',
    'via-amber-950',
    'via-yellow-50',
    'via-yellow-100',
    'via-yellow-200',
    'via-yellow-300',
    'via-yellow-400',
    'via-yellow-500',
    'via-yellow-600',
    'via-yellow-700',
    'via-yellow-800',
    'via-yellow-900',
    'via-yellow-950',
    'via-lime-50',
    'via-lime-100',
    'via-lime-200',
    'via-lime-300',
    'via-lime-400',
    'via-lime-500',
    'via-lime-600',
    'via-lime-700',
    'via-lime-800',
    'via-lime-900',
    'via-lime-950',
    'via-green-50',
    'via-green-100',
    'via-green-200',
    'via-green-300',
    'via-green-400',
    'via-green-500',
    'via-green-600',
    'via-green-700',
    'via-green-800',
    'via-green-900',
    'via-green-950',
    'via-emerald-50',
    'via-emerald-100',
    'via-emerald-200',
    'via-emerald-300',
    'via-emerald-400',
    'via-emerald-500',
    'via-emerald-600',
    'via-emerald-700',
    'via-emerald-800',
    'via-emerald-900',
    'via-emerald-950',
    'via-teal-50',
    'via-teal-100',
    'via-teal-200',
    'via-teal-300',
    'via-teal-400',
    'via-teal-500',
    'via-teal-600',
    'via-teal-700',
    'via-teal-800',
    'via-teal-900',
    'via-teal-950',
    'via-cyan-50',
    'via-cyan-100',
    'via-cyan-200',
    'via-cyan-300',
    'via-cyan-400',
    'via-cyan-500',
    'via-cyan-600',
    'via-cyan-700',
    'via-cyan-800',
    'via-cyan-900',
    'via-cyan-950',
    'via-sky-50',
    'via-sky-100',
    'via-sky-200',
    'via-sky-300',
    'via-sky-400',
    'via-sky-500',
    'via-sky-600',
    'via-sky-700',
    'via-sky-800',
    'via-sky-900',
    'via-sky-950',
    'via-blue-50',
    'via-blue-100',
    'via-blue-200',
    'via-blue-300',
    'via-blue-400',
    'via-blue-500',
    'via-blue-600',
    'via-blue-700',
    'via-blue-800',
    'via-blue-900',
    'via-blue-950',
    'via-indigo-50',
    'via-indigo-100',
    'via-indigo-200',
    'via-indigo-300',
    'via-indigo-400',
    'via-indigo-500',
    'via-indigo-600',
    'via-indigo-700',
    'via-indigo-800',
    'via-indigo-900',
    'via-indigo-950',
    'via-violet-50',
    'via-violet-100',
    'via-violet-200',
    'via-violet-300',
    'via-violet-400',
    'via-violet-500',
    'via-violet-600',
    'via-violet-700',
    'via-violet-800',
    'via-violet-900',
    'via-violet-950',
    'via-purple-50',
    'via-purple-100',
    'via-purple-200',
    'via-purple-300',
    'via-purple-400',
    'via-purple-500',
    'via-purple-600',
    'via-purple-700',
    'via-purple-800',
    'via-purple-900',
    'via-purple-950',
    'via-fuchsia-50',
    'via-fuchsia-100',
    'via-fuchsia-200',
    'via-fuchsia-300',
    'via-fuchsia-400',
    'via-fuchsia-500',
    'via-fuchsia-600',
    'via-fuchsia-700',
    'via-fuchsia-800',
    'via-fuchsia-900',
    'via-fuchsia-950',
    'via-pink-50',
    'via-pink-100',
    'via-pink-200',
    'via-pink-300',
    'via-pink-400',
    'via-pink-500',
    'via-pink-600',
    'via-pink-700',
    'via-pink-800',
    'via-pink-900',
    'via-pink-950',
    'via-rose-50',
    'via-rose-100',
    'via-rose-200',
    'via-rose-300',
    'via-rose-400',
    'via-rose-500',
    'via-rose-600',
    'via-rose-700',
    'via-rose-800',
    'via-rose-900',
    'via-rose-950',
    'via-0%',
    'via-5%',
    'via-10%',
    'via-15%',
    'via-20%',
    'via-25%',
    'via-30%',
    'via-35%',
    'via-40%',
    'via-45%',
    'via-50%',
    'via-55%',
    'via-60%',
    'via-65%',
    'via-70%',
    'via-75%',
    'via-80%',
    'via-85%',
    'via-90%',
    'via-95%',
    'via-100%',
    'to-inherit',
    'to-current',
    'to-transparent',
    'to-black',
    'to-white',
    'to-slate-50',
    'to-slate-100',
    'to-slate-200',
    'to-slate-300',
    'to-slate-400',
    'to-slate-500',
    'to-slate-600',
    'to-slate-700',
    'to-slate-800',
    'to-slate-900',
    'to-slate-950',
    'to-gray-50',
    'to-gray-100',
    'to-gray-200',
    'to-gray-300',
    'to-gray-400',
    'to-gray-500',
    'to-gray-600',
    'to-gray-700',
    'to-gray-800',
    'to-gray-900',
    'to-gray-950',
    'to-zinc-50',
    'to-zinc-100',
    'to-zinc-200',
    'to-zinc-300',
    'to-zinc-400',
    'to-zinc-500',
    'to-zinc-600',
    'to-zinc-700',
    'to-zinc-800',
    'to-zinc-900',
    'to-zinc-950',
    'to-neutral-50',
    'to-neutral-100',
    'to-neutral-200',
    'to-neutral-300',
    'to-neutral-400',
    'to-neutral-500',
    'to-neutral-600',
    'to-neutral-700',
    'to-neutral-800',
    'to-neutral-900',
    'to-neutral-950',
    'to-stone-50',
    'to-stone-100',
    'to-stone-200',
    'to-stone-300',
    'to-stone-400',
    'to-stone-500',
    'to-stone-600',
    'to-stone-700',
    'to-stone-800',
    'to-stone-900',
    'to-stone-950',
    'to-red-50',
    'to-red-100',
    'to-red-200',
    'to-red-300',
    'to-red-400',
    'to-red-500',
    'to-red-600',
    'to-red-700',
    'to-red-800',
    'to-red-900',
    'to-red-950',
    'to-orange-50',
    'to-orange-100',
    'to-orange-200',
    'to-orange-300',
    'to-orange-400',
    'to-orange-500',
    'to-orange-600',
    'to-orange-700',
    'to-orange-800',
    'to-orange-900',
    'to-orange-950',
    'to-amber-50',
    'to-amber-100',
    'to-amber-200',
    'to-amber-300',
    'to-amber-400',
    'to-amber-500',
    'to-amber-600',
    'to-amber-700',
    'to-amber-800',
    'to-amber-900',
    'to-amber-950',
    'to-yellow-50',
    'to-yellow-100',
    'to-yellow-200',
    'to-yellow-300',
    'to-yellow-400',
    'to-yellow-500',
    'to-yellow-600',
    'to-yellow-700',
    'to-yellow-800',
    'to-yellow-900',
    'to-yellow-950',
    'to-lime-50',
    'to-lime-100',
    'to-lime-200',
    'to-lime-300',
    'to-lime-400',
    'to-lime-500',
    'to-lime-600',
    'to-lime-700',
    'to-lime-800',
    'to-lime-900',
    'to-lime-950',
    'to-green-50',
    'to-green-100',
    'to-green-200',
    'to-green-300',
    'to-green-400',
    'to-green-500',
    'to-green-600',
    'to-green-700',
    'to-green-800',
    'to-green-900',
    'to-green-950',
    'to-emerald-50',
    'to-emerald-100',
    'to-emerald-200',
    'to-emerald-300',
    'to-emerald-400',
    'to-emerald-500',
    'to-emerald-600',
    'to-emerald-700',
    'to-emerald-800',
    'to-emerald-900',
    'to-emerald-950',
    'to-teal-50',
    'to-teal-100',
    'to-teal-200',
    'to-teal-300',
    'to-teal-400',
    'to-teal-500',
    'to-teal-600',
    'to-teal-700',
    'to-teal-800',
    'to-teal-900',
    'to-teal-950',
    'to-cyan-50',
    'to-cyan-100',
    'to-cyan-200',
    'to-cyan-300',
    'to-cyan-400',
    'to-cyan-500',
    'to-cyan-600',
    'to-cyan-700',
    'to-cyan-800',
    'to-cyan-900',
    'to-cyan-950',
    'to-sky-50',
    'to-sky-100',
    'to-sky-200',
    'to-sky-300',
    'to-sky-400',
    'to-sky-500',
    'to-sky-600',
    'to-sky-700',
    'to-sky-800',
    'to-sky-900',
    'to-sky-950',
    'to-blue-50',
    'to-blue-100',
    'to-blue-200',
    'to-blue-300',
    'to-blue-400',
    'to-blue-500',
    'to-blue-600',
    'to-blue-700',
    'to-blue-800',
    'to-blue-900',
    'to-blue-950',
    'to-indigo-50',
    'to-indigo-100',
    'to-indigo-200',
    'to-indigo-300',
    'to-indigo-400',
    'to-indigo-500',
    'to-indigo-600',
    'to-indigo-700',
    'to-indigo-800',
    'to-indigo-900',
    'to-indigo-950',
    'to-violet-50',
    'to-violet-100',
    'to-violet-200',
    'to-violet-300',
    'to-violet-400',
    'to-violet-500',
    'to-violet-600',
    'to-violet-700',
    'to-violet-800',
    'to-violet-900',
    'to-violet-950',
    'to-purple-50',
    'to-purple-100',
    'to-purple-200',
    'to-purple-300',
    'to-purple-400',
    'to-purple-500',
    'to-purple-600',
    'to-purple-700',
    'to-purple-800',
    'to-purple-900',
    'to-purple-950',
    'to-fuchsia-50',
    'to-fuchsia-100',
    'to-fuchsia-200',
    'to-fuchsia-300',
    'to-fuchsia-400',
    'to-fuchsia-500',
    'to-fuchsia-600',
    'to-fuchsia-700',
    'to-fuchsia-800',
    'to-fuchsia-900',
    'to-fuchsia-950',
    'to-pink-50',
    'to-pink-100',
    'to-pink-200',
    'to-pink-300',
    'to-pink-400',
    'to-pink-500',
    'to-pink-600',
    'to-pink-700',
    'to-pink-800',
    'to-pink-900',
    'to-pink-950',
    'to-rose-50',
    'to-rose-100',
    'to-rose-200',
    'to-rose-300',
    'to-rose-400',
    'to-rose-500',
    'to-rose-600',
    'to-rose-700',
    'to-rose-800',
    'to-rose-900',
    'to-rose-950',
    'to-0%',
    'to-5%',
    'to-10%',
    'to-15%',
    'to-20%',
    'to-25%',
    'to-30%',
    'to-35%',
    'to-40%',
    'to-45%',
    'to-50%',
    'to-55%',
    'to-60%',
    'to-65%',
    'to-70%',
    'to-75%',
    'to-80%',
    'to-85%',
    'to-90%',
    'to-95%',
    'to-100%',
]
