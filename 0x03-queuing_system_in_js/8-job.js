export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw Error(`${jobs} is not an array`);
  }
  jobs.forEach((element) => {
    const job = queue
      .create("push_notification_code_3", element)
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${job.id}`);
        }
      });

      job.on("complete", () => {
        console.log(`Notification job ${job.id} completed`);
      });
    
      job.on("failed", (err) => {
        console.log(`Notification job ${job.id} failed: ${err}`);
      });
    
      job.on("progress", (progress, _data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
  });
}
