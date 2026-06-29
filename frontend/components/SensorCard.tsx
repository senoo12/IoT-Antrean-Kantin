"use client";

interface Props {
    value: number;
}

export default function SensorCard({ value }: Props) {

    return (

        <div className="bg-white rounded-2xl shadow-md border border-slate-200 p-6">

            <p className="text-gray-500 text-sm mb-4">
                Jarak Sensor
            </p>

            <div className="flex items-end gap-2">

                <span className="text-6xl font-bold text-indigo-600">
                    {value.toFixed(0)}
                </span>

                <span className="text-2xl mb-2 text-gray-500">
                    cm
                </span>

            </div>

            <div className="mt-6 pt-4 border-t">

                <p className="text-gray-500">
                    Ultrasonic HC-SR04
                </p>

            </div>

        </div>

    );

}