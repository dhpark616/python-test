// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: msg_type_api.proto
#pragma warning disable 1591, 0612, 3021
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Msg {

  /// <summary>Holder for reflection information generated from msg_type_api.proto</summary>
  public static partial class MsgTypeApiReflection {

    #region Descriptor
    /// <summary>File descriptor for msg_type_api.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static MsgTypeApiReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "ChJtc2dfdHlwZV9hcGkucHJvdG8SA21zZyr8AQoIdHlwZV9hcGkSCAoEbm9u",
            "ZRAAEhAKC3RfbG9naW5fcmVxEN1WEhAKC3RfbG9naW5fYWNrEN5WEhgKE3Rf",
            "Z2V0X2NoYXJfbGlzdF9yZXEQwVcSGAoTdF9nZXRfY2hhcl9saXN0X2FjaxDC",
            "VxIWChF0X2NyZWF0ZV9jaGFyX3JlcRDDVxIWChF0X2NyZWF0ZV9jaGFyX2Fj",
            "axDEVxIWChF0X2RlbGV0ZV9jaGFyX3JlcRDFVxIWChF0X2RlbGV0ZV9jaGFy",
            "X2FjaxDGVxIWChF0X3NlbGVjdF9jaGFyX3JlcRDHVxIWChF0X3NlbGVjdF9j",
            "aGFyX2FjaxDIV2IGcHJvdG8z"));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { },
          new pbr::GeneratedClrTypeInfo(new[] {typeof(global::Msg.type_api), }, null));
    }
    #endregion

  }
  #region Enums
  /// <summary>
  /// 10000
  /// </summary>
  public enum type_api {
    [pbr::OriginalName("none")] None = 0,
    /// <summary>
    /// 11 : system
    /// </summary>
    [pbr::OriginalName("t_login_req")] TLoginReq = 11101,
    [pbr::OriginalName("t_login_ack")] TLoginAck = 11102,
    /// <summary>
    /// 12 : lobby
    /// </summary>
    [pbr::OriginalName("t_get_char_list_req")] TGetCharListReq = 11201,
    [pbr::OriginalName("t_get_char_list_ack")] TGetCharListAck = 11202,
    [pbr::OriginalName("t_create_char_req")] TCreateCharReq = 11203,
    [pbr::OriginalName("t_create_char_ack")] TCreateCharAck = 11204,
    [pbr::OriginalName("t_delete_char_req")] TDeleteCharReq = 11205,
    [pbr::OriginalName("t_delete_char_ack")] TDeleteCharAck = 11206,
    [pbr::OriginalName("t_select_char_req")] TSelectCharReq = 11207,
    [pbr::OriginalName("t_select_char_ack")] TSelectCharAck = 11208,
  }

  #endregion

}

#endregion Designer generated code