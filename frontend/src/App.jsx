import OrdersList from "./components/OrdersList.jsx";

export default function App() {
  return (
    <main style={{ fontFamily: "system-ui, sans-serif", padding: "2rem" }}>
      <h1>Orders</h1>
      <OrdersList />
    </main>
  );
}
