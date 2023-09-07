const submitButton = document.querySelector("button");

submitButton.addEventListener("click", async () => {
  const r = await fetch("/push", {
    method: "POST",
    headers: {
      "Content-type": "application/json",
    },
    body: JSON.stringify({
      user_id: document?.querySelector("[name=user_id]")?.value ?? null,
      message: document?.querySelector("[name=message]")?.value,
    }),
  });
  if (r.status) {
    document.querySelector("p").innerHTML = await r.text();
  }
});
