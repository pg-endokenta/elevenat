import React, { useEffect, useState } from 'react';
import type { UserStatus } from './types';
import { UserIcon } from './components/UserIcon';
import { Legend } from './components/Legend';

const API_URL = 'https://studious-space-system-xg6w5v7x5jrh6qxq-8000.app.github.dev/attendance/logs/now/';
// const API_URL = "http://127.0.0.1:8000/attendance/logs/now/";

// const generateDummyData = (): UserStatus[] => {
//   const now = new Date();
//   return Array.from({ length: 11 }, (_, i) => ({
//     id: i + 1,
//     name: `${i}`,
//     lastSeen: new Date(now.getTime() - Math.random() * 250 * 60 * 1000), // 0〜250分前
//   }));
// };

const App: React.FC = () => {
  const [users, setUsers] = useState<UserStatus[]>([]);
  const [now, setNow] = useState(new Date());

  // データ取得関数
  const fetchUserStatuses = async () => {
  try {
    const res = await fetch(API_URL, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({}), // 必要なリクエストボディがあればここに
    });

    const data = await res.json();

    const now = new Date();
    const parsed: UserStatus[] = data.map((user: any) => ({
      id: user.id,
      name: user.name,
      lastSeen: new Date(now.getTime() - user.last_seen * 60 * 1000),
    }));

    setUsers(parsed);
  } catch (error) {
    console.error('データ取得失敗:', error);
  }
};

  useEffect(() => {
    fetchUserStatuses(); // 初回取得
    const refresh = setInterval(fetchUserStatuses, 60 * 1000); // 1分おきに取得
    const tick = setInterval(() => setNow(new Date()), 30 * 1000); // 時計更新

    return () => {
      clearInterval(refresh);
      clearInterval(tick);
    };
  }, []);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-white">
      <h1 className="text-2xl mb-4">入退出ステータス</h1>
      <div className="grid grid-cols-6 gap-4">
        {users.map((user) => (
          <UserIcon key={user.id} user={user} now={now} />
        ))}
      </div>
      <Legend />
    </div>
  );
};


export default App;
