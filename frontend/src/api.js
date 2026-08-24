const BASE_URL = "http://localhost:8010";

export async function fetchOrders() {
  const res = await fetch(`${BASE_URL}/orders`);
  if (!res.ok) {
    throw new Error(`Failed to load orders: ${res.status}`);
  }
  return res.json();
}

export async function fetchUsers() {
  const res = await fetch(`${BASE_URL}/users`);
  if (!res.ok) {
    throw new Error(`Failed to load users: ${res.status}`);
  }
  return res.json();
}
