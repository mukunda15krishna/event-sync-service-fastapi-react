import { useEffect, useMemo, useState } from "react";
import axios from "axios";

function App() {
  const [meetings, setMeetings] = useState([]);
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("ALL");

  useEffect(() => {
    axios
      .get("http://127.0.0.1:8000/meetings")
      .then((res) => {
  console.log(res.data[0]);
  setMeetings(res.data);
});
  }, []);

  const filteredMeetings = useMemo(() => {
    return meetings.filter((meeting) => {
      const text =
        (
          meeting.subject +
          meeting.client_name +
          meeting.client_company
        ).toLowerCase();

      const matchesSearch = text.includes(search.toLowerCase());

      if (filter === "MATCHED")
        return meeting.matched && matchesSearch;

      if (filter === "UNMATCHED")
        return !meeting.matched && matchesSearch;

      if (filter === "CONFLICT")
        return meeting.conflict && matchesSearch;

      return matchesSearch;
    });
  }, [meetings, search, filter]);

  const total = meetings.length;
  const matched = meetings.filter((m) => m.matched).length;
  const unmatched = meetings.filter((m) => !m.matched).length;
  const conflicts = meetings.filter((m) => m.conflict).length;

  return (
    <div
      style={{
        padding: 30,
        background: "#f4f6f9",
        minHeight: "100vh",
        fontFamily: "Arial",
      }}
    >
      <h1>Event Sync Service</h1>

      <div
        style={{
          display: "flex",
          gap: 20,
          marginBottom: 25,
        }}
      >
        <Card title="Total Records" value={total} />
        <Card title="Matched" value={matched} />
        <Card title="Unmatched" value={unmatched} />
        <Card title="Conflicts" value={conflicts} />
      </div>

      <div
        style={{
          display: "flex",
          gap: 15,
          marginBottom: 20,
        }}
      >
        <input
          placeholder="Search..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          style={{
            padding: 10,
            width: 300,
          }}
        />

        <select
          value={filter}
          onChange={(e) => setFilter(e.target.value)}
          style={{
            padding: 10,
          }}
        >
          <option value="ALL">All</option>
          <option value="MATCHED">Matched</option>
          <option value="UNMATCHED">Unmatched</option>
          <option value="CONFLICT">Conflict</option>
        </select>
      </div>

      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          background: "white",
        }}
      >
        <thead
          style={{
            background: "#1f2937",
            color: "white",
          }}
        >
          <tr>
            <th style={cell}>Record ID</th>
            <th style={cell}>Subject</th>
            <th style={cell}>Client</th>
            <th style={cell}>Company</th>
            <th style={cell}>Date</th>
            <th style={cell}>Time</th>
            <th style={cell}>Source</th>
            <th style={cell}>Status</th>
          </tr>
        </thead>

        <tbody>
          {filteredMeetings.map((meeting, index) => (
            <tr
              key={meeting.crm_id}
              style={{
                background: meeting.conflict
                  ? "#ffe4e6"
                  : "white",
              }}
            >
              <td style={cell}>{meeting.crm_id}</td>
              <td style={cell}>{meeting.subject}</td>
              <td style={cell}>{meeting.client_name}</td>
              <td style={cell}>{meeting.client_company}</td>
              <td style={cell}>{meeting.meeting_date}</td>
              <td style={cell}>{meeting.meeting_time}</td>

              <td style={cell}>
                {meeting.source || "N/A"}
              </td>

              <td style={cell}>
                {meeting.conflict
                  ? "⚠️ Conflict"
                  : meeting.matched
                  ? "✅ Matched"
                  : "❌ Unmatched"}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

function Card({ title, value }) {
  return (
    <div
      style={{
        background: "white",
        padding: 20,
        width: 170,
        borderRadius: 8,
        boxShadow: "0 2px 8px rgba(0,0,0,.1)",
      }}
    >
      <h3>{title}</h3>
      <h2>{value}</h2>
    </div>
  );
}

const cell = {
  border: "1px solid #ddd",
  padding: 10,
};

export default App;