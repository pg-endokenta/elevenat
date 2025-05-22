

import { useEffect, useState } from 'react';
import type { UserStatus } from '../types';
import { UserIcon } from '../components/UserIcon';
import { Legend } from '../components/Legend';

const API_URL = "/attendance/logs/now/";

function getCookie(name: string) {
  const cookieValue = document.cookie
    .split('; ')
    .find((row) => row.startsWith(name + '='));
  return cookieValue ? decodeURIComponent(cookieValue.split('=')[1]) : '';
}

export const Room = () => {
    const [users, setUsers] = useState<UserStatus[]>([]);
    const [now, setNow] = useState(new Date());
    const csrfToken = getCookie('csrftoken');

    // データ取得関数
    const fetchUserStatuses = async () => {
    try {
    const res = await fetch(API_URL, {
        method: 'POST',
        credentials: 'include',
        headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken,
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