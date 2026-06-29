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

import { getQueueLabel } from "@/utils/queue";

type Sensor = {
    id: number;
    distance_cm: number;
    created_at: string;
};

interface Props {
    data: Sensor[];
}

export default function QueueChart({ data }: Props) {

    const chartData = data.map(item => ({

        id: item.id,

        value:
            getQueueLabel(item.distance_cm) === "Kosong"
                ? 0
                : getQueueLabel(item.distance_cm) === "Ada Antrean"
                    ? 1
                    : 2

    }));

    return (

        <div className="bg-white rounded-2xl shadow-lg p-6">

            <h2 className="text-lg font-semibold mb-5 text-slate-700">

                🚶 Grafik Kondisi Antrean

            </h2>

            <ResponsiveContainer
                width="100%"
                height={350}
            >

                <LineChart data={chartData}>

                    <CartesianGrid strokeDasharray="5 5" />

                    <XAxis
                        dataKey="id"
                        tick={{ fontSize: 12 }}
                    />

                    <YAxis
                        ticks={[0, 1, 2]}
                        domain={[0, 2]}
                        tickFormatter={(value) => {

                            switch (value) {

                                case 0:
                                    return "Kosong";

                                case 1:
                                    return "Antrean";

                                default:
                                    return "Panjang";

                            }

                        }}
                    />

                    <Tooltip
                        formatter={(value) => {

                            switch (value) {

                                case 0:
                                    return "Kosong";

                                case 1:
                                    return "Ada Antrean";

                                default:
                                    return "Antrean Panjang";

                            }

                        }}
                    />

                    <Line
                        dataKey="value"
                        stroke="#ef4444"
                        strokeWidth={3}
                        dot={{ r: 4 }}
                        activeDot={{ r: 7 }}
                        type="stepAfter"
                    />

                </LineChart>

            </ResponsiveContainer>

        </div>

    );

}