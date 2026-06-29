"use client";

import SensorCard from "@/components/SensorCard";
import LastUpdate from "@/components/LastUpdate";
import SensorChart from "@/components/SensorChart";
import QueueChart from "@/components/QueueChart";

import { useSensor } from "@/hooks/useSensor";
import StatusCard from "@/components/StatusCard";
import { getQueueLabel } from "@/utils/queue";

export default function Home() {
  const {
    latest,
    history,
    loading,
    error,
    refresh
  } = useSensor();

  if (loading) {
    return (
      <div className="h-screen flex items-center justify-center">
        Loading...
      </div>
    );
  }

  if (error) {
    return (
      <div className="h-screen flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-bold mb-2">
            Belum Ada Data
          </h2>

          <p className="text-gray-500">
            Jalankan ESP32 atau kirim data sensor terlebih dahulu.
          </p>
        </div>
      </div>
    );
  }

  return (
    <main className="min-h-screen bg-slate-100">
      <div className="max-w-7xl mx-auto px-8 py-10">

        <div className="flex justify-between items-start mb-10">

          <div>
            <h1 className="text-5xl font-bold text-slate-900">
              Dashboard IoT Antrean Kantin
            </h1>

            <p className="text-slate-500 mt-2">
              Monitoring kondisi antrean secara realtime
            </p>
          </div>

          <button
            onClick={refresh}
            className="rounded-xl bg-indigo-600 hover:bg-indigo-700
                   text-white px-6 py-3 font-medium shadow"
          >
            Refresh Data
          </button>

        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">

          <StatusCard
            label={getQueueLabel(latest!.distance_cm)}
          />

          <SensorCard
            value={latest!.distance_cm}
          />

          <LastUpdate
            time={latest!.created_at}
          />

        </div>

        <div className="grid grid-cols-1 xl:grid-cols-2 gap-8">

          <SensorChart data={history} />

          <QueueChart data={history} />
          

        </div>

      </div>
    </main>
  );
}