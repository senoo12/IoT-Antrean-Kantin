export function getQueueLabel(distance: number): string {

    if (distance > 120) {
        return "Kosong";
    }

    if (distance >= 50) {
        return "Ada Antrean";
    }

    return "Antrean Panjang";
}