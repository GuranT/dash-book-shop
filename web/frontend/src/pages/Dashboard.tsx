import { useEffect, useState } from "react"
import axios from "axios"

export default function Dashboard() {
  const [stats, setStats] = useState({ sales: 0, orders: 0, products: 0, tickets: 0 })

  useEffect(() => {
    axios.get("/api/stats").then(r => setStats(r.data))
  }, [])

  return (
    <div className="p-8 bg-gray-50 min-h-screen">
      <h1 className="text-4xl font-bold mb-8 text-gray-800">Панель управления</h1>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
        <div className="border-emerald-200 bg-emerald-50 p-6 rounded-lg">
          <div className="text-sm font-medium text-emerald-700 mb-2">Продажи</div>
          <div className="text-3xl font-bold text-emerald-700">${stats.sales.toFixed(2)}</div>
          <p className="text-xs text-emerald-600">Всего заработано</p>
        </div>

        <div className="border-blue-200 bg-blue-50 p-6 rounded-lg">
          <div className="text-sm font-medium text-blue-700 mb-2">Заказы</div>
          <div className="text-3xl font-bold text-blue-700">{stats.orders}</div>
          <p className="text-xs text-blue-600">Оплаченных</p>
        </div>

        <div className="border-purple-200 bg-purple-50 p-6 rounded-lg">
          <div className="text-sm font-medium text-purple-700 mb-2">Товары</div>
          <div className="text-3xl font-bold text-purple-700">{stats.products}</div>
          <p className="text-xs text-purple-600">В каталоге</p>
        </div>

        <div className="border-orange-200 bg-orange-50 p-6 rounded-lg">
          <div className="text-sm font-medium text-orange-700 mb-2">Тикеты</div>
          <div className="text-3xl font-bold text-orange-700">{stats.tickets}</div>
          <p className="text-xs text-orange-600">Не отвеченные</p>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-white rounded-xl shadow-lg p-6">
          <h2 className="text-xl font-semibold mb-4">Последние заказы</h2>
          <p className="text-gray-500">Таблица заказов (API в разработке)</p>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-6">
          <h2 className="text-xl font-semibold mb-4">Продажи за неделю</h2>
          <p className="text-gray-500">График (Chart.js в разработке)</p>
        </div>
      </div>
    </div>
  )
}
