rpc.exports = {
  encrypt(string, offset) {
    let token = null;
    Java.perform(function () {
      var util = Java.use("com.goldze.mvvmhabit.utils.NativeUtils").$new();
      token = util.encrypt(string, offset);
    });
    return token;
  },
};
