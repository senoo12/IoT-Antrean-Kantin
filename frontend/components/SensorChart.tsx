"use client";

import {
    ResponsiveContainer,
    LineChart,
    Line,
    XAxis,
    YAxis,
    Tooltip,
    CartesianGrid
} from "recharts";

import { SensorData } from "@/types/sensor";

interface Props {
    data: SensorData[];
}

export default function SensorChart({ data }: Props) {

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-lg font-semibold mb-5 text-slate-700">

                📏 Grafik Perubahan Jarak

            </h2>

            <ResponsiveContainer
                width="100%"
                height={350}
            >

                <LineChart data={data}>

                    <CartesianGrid strokeDasharray="5 5" />

                    <XAxis
                        dataKey="id"
                        tick={{ fontSize: 12 }}
                    />

                    <YAxis
                        label={{
                            value: "cm",
                            angle: -90,
                            position: "insideLeft"
                        }}
                    />

                    <Tooltip />

                    <Line
                        dataKey="distance_cm"
                        stroke="#2563eb"
                        strokeWidth={3}
                        dot={{ r: 4 }}
                        activeDot={{ r: 7 }}
                        type="monotone"
                    />

                </LineChart>

            </ResponsiveContainer>

        </div>

    );

}