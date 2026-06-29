"use client";

import { useEffect, useState } from "react";
import { api } from "@/lib/api";
import { SensorData } from "@/types/sensor";

export function useSensor() {
    const [latest, setLatest] = useState<SensorData | null>(null);
    const [history, setHistory] = useState<SensorData[]>([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");

    const load = async () => {
        try {
            setLoading(true);

            const [latestRes, historyRes] = await Promise.all([
                api.get("/sensor/latest"),
                api.get("/sensor/data"),
            ]);

            setLatest(latestRes.data);
            setHistory(historyRes.data.reverse());

            setError("");
        } catch (err: any) {
            if (err.response?.status === 404) {
                setLatest(null);
                setHistory([]);
                setError("Belum ada data sensor.");
            } else {
                setError("Gagal mengambil data.");
            }
        } finally {
            setLoading(false);
        }
    };

    useEffect(() => {
        load();
    }, []);

    return {
        latest,
        history,
        loading,
        error,
        refresh: load, // expose fungsi refresh
    };
}