import { BucketVersioningStateArgs } from "../../bucketArgs";

export default {
  public: true,
  versioning: BucketVersioningStateArgs.Enabled,
  encryption: {
    enabled: true,
    customKeyId: "custom-key",
  },
};
