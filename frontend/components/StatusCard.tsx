"use client";

interface Props {
    label: string;
}

export default function StatusCard({ label }: Props) {

    const getColor = () => {
        switch (label) {
            case "Kosong":
                return "bg-green-100 text-green-700";

            case "Ada Antrean":
                return "bg-yellow-100 text-yellow-700";

            default:
                return "bg-red-100 text-red-700";
        }
    };

    const getIcon = () => {
        switch (label) {
            case "Kosong":
                return "🟢";

            case "Ada Antrean":
                return "🟡";

            default:
                return "🔴";
        }
    };

    return (
        <div className="bg-white rounded-2xl shadow-md border border-slate-200 p-6">

            <p className="text-gray-500 text-sm mb-4">
                Status Antrean
            </p>

            <h2 className="text-3xl font-bold text-slate-800">
                {label}
            </h2>

            <div
                className={`inline-flex mt-5 px-4 py-2 rounded-full font-medium ${getColor()}`}
            >
                {getIcon()} {label}
            </div>

        </div>
    );
}