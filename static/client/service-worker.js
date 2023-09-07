self.addEventListener("push", function (event) {
  const payload = event.data ? event.data.text() : "no payload";
  event.waitUntil(
    self.registration.showNotification("Mehdi Abdi", {
      body: payload,
      icon: "https://cdn.mehdiabdi.com/maskable_icon_x384.png",
    })
  );
});

self.addEventListener("fetch", (event) => {
  return;
});
