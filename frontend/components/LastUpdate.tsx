"use client";

interface Props {
    time: string;
}

export default function LastUpdate({ time }: Props) {

    const date = new Date(time);

    return (

        <div className="bg-white rounded-2xl shadow-md border border-slate-200 p-6">

            <p className="text-gray-500 text-sm mb-4">
                Pembaruan Terakhir
            </p>

            <h2 className="text-5xl font-bold text-slate-800">
                {date.toLocaleTimeString("id-ID")}
            </h2>

            <p className="mt-3 text-gray-500">
                {date.toLocaleDateString("id-ID", {
                    weekday: "long",
                    day: "numeric",
                    month: "long",
                    year: "numeric",
                })}
            </p>

        </div>

    );

}