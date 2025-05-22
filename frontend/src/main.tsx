import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Routes, Route } from "react-router";
import './index.css'
// import { UserDetail } from './pages/UserDetail';
// import { Room } from './pages/Room.tsx';
import PresenceStats from './pages/PresenceStats.tsx';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        {/* <Route path="/frontend/room" element={<Room />} /> */}
        <Route path="/frontend/presence-stats" element={<PresenceStats />} />
        {/* <Route path="/user/:id" element={<UserDetail />} /> */}
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
