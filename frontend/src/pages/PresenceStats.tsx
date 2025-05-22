// src/pages/PresenceStats.tsx

import { useEffect, useState } from "react";
import HomeButton from "../components/HomeButton";

interface PresenceStat {
  user_id: number;
  username: string;
  last_seen: string | null;
  today_count: number;
  total_count: number;
}

function getRowBgColor(dateString: string | null): string {
  if (!dateString) return "bg-red-100";

  const date = new Date(dateString);
  const now = new Date();
  const diffMin = Math.floor((now.getTime() - date.getTime()) / 60000);

  if (diffMin < 5) return "bg-green-100";
  if (diffMin < 30) return "bg-yellow-100";
  return "bg-gray-100";
}

function formatRelativeTime(dateString: string | null): string {
  if (!dateString) return "未検出";

  const date = new Date(dateString);
  const now = new Date();
  const diffMs = now.getTime() - date.getTime();

  const diffSec = Math.floor(diffMs / 1000);
  const diffMin = Math.floor(diffSec / 60);
  const diffHour = Math.floor(diffMin / 60);
  const diffDay = Math.floor(diffHour / 24);

  if (diffMin < 1) return "たった今";
  if (diffMin < 60) return `${diffMin}分前`;
  if (diffHour < 24) return `${diffHour}時間${diffMin % 60}分前`;
  return `${diffDay}日前`;
}

export default function PresenceStats() {
  const [stats, setStats] = useState<PresenceStat[]>([]);
  const [error, setError] = useState("");

  useEffect(() => {
    (async () => {
      try {
        const res = await fetch("/api/presence-stats/");
        if (!res.ok) throw new Error("Failed to fetch");
        const data = await res.json();
        setStats(data);
      } catch (e) {
        setError("取得に失敗しました");
      }
    })();
  }, []);

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">全ユーザーの出席状況</h1>
      {error && <div className="text-red-500">{error}</div>}
      <table className="table-auto w-full border-collapse border border-gray-300">
        <thead>
          <tr className="bg-gray-100">
            <th className="border px-4 py-2">ユーザー名</th>
            <th className="border px-4 py-2">最終検出</th>
            <th className="border px-4 py-2">今日の滞在時間[分]</th>
            <th className="border px-4 py-2">総滞在時間[分]</th>
          </tr>
        </thead>
        <tbody>
          {stats.map((s) => (
            <tr key={s.user_id} className={getRowBgColor(s.last_seen)}>
              <td className="border px-4 py-2">{s.username}</td>
              <td className="border px-4 py-2">
                {formatRelativeTime(s.last_seen)}
              </td>
              <td className="border px-4 py-2 text-center">{s.today_count}</td>
              <td className="border px-4 py-2 text-center">{s.total_count}</td>
            </tr>
          ))}
        </tbody>
      </table>
      <HomeButton />
    </div>

  );
}
