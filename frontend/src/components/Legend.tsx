// components/Legend.tsx
import React from 'react';

export const Legend: React.FC = () => {
  const levels = [
    { color: 'bg-green-700', label: '0–15分' },
    { color: 'bg-emerald-600', label: '15–45分' },
    { color: 'bg-lime-500', label: '45–90分' },
    { color: 'bg-zinc-400', label: '90–150分' },
    { color: 'bg-gray-400', label: '150–180分' },
    { color: 'bg-gray-300', label: '180分以上' },
  ];

  return (
    <div className="mt-8 w-full max-w-md">
      <h2 className="text-lg font-semibold mb-2 text-center">時間経過と色の関係</h2>
      <div className="grid grid-cols-6 gap-2 text-xs text-center">
        {levels.map((level, index) => (
          <div key={index}>
            <div className={`w-10 h-10 mx-auto rounded-full ${level.color}`}></div>
            <div>{level.label}</div>
          </div>
        ))}
      </div>
    </div>
  );
};
