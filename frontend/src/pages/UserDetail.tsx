import { useParams, useNavigate } from 'react-router';

export const UserDetail = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-4">
      <h2 className="text-2xl font-bold mb-4">User Detail</h2>
      <p className="mb-8">ユーザーID: {id}</p>
      <p className="mb-8">詳細ページは後々作成します</p>

      <button
        onClick={() => navigate(-1)}
        className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 transition"
      >
        戻る
      </button>
    </div>
  );
};
