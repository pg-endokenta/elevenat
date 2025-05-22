import React from 'react';
import type { UserStatus } from '../types';
import { useNavigate } from 'react-router';

interface Props {
  user: UserStatus;
  now: Date;
}

const getColorClass = (lastSeen: Date, now: Date): string => {
  const diffMinutes = (now.getTime() - new Date(lastSeen).getTime()) / 60000;
  if (diffMinutes <= 15) return 'bg-green-700';
  if (diffMinutes <= 45) return 'bg-emerald-600';
  if (diffMinutes <= 90) return 'bg-lime-500';
  if (diffMinutes <= 150) return 'bg-zinc-400';
  if (diffMinutes <= 180) return 'bg-gray-400';
  return 'bg-gray-300';
};

export const UserIcon: React.FC<Props> = ({ user, now }) => {
  const navigate = useNavigate();
  const colorClass = getColorClass(user.lastSeen, now);

  const handleClick = () => {
    navigate(`/user/${user.id}`);
  };

  return (
    <div
      className={`w-16 h-16 rounded-full flex items-center justify-center text-white cursor-pointer ${colorClass}`}
      onClick={handleClick}
      title={`Last seen: ${user.lastSeen.toLocaleTimeString()}`}
    >
      {/* {user.name[0]} */}
      {user.name.length < 7 ? user.name : user.name.slice(0, 7) + '...'}
    </div>
  );
};
