# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class QueryAlarmHistoryRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'QueryAlarmHistory')

	def get_Cursor(self):
		return self.get_query_params().get('Cursor')

	def set_Cursor(self,Cursor):
		self.add_query_param('Cursor',Cursor)

	def get_ResourceOwnerId(self):
		return self.get_query_params().get('ResourceOwnerId')

	def set_ResourceOwnerId(self,ResourceOwnerId):
		self.add_query_param('ResourceOwnerId',ResourceOwnerId)

	def get_Size(self):
		return self.get_query_params().get('Size')

	def set_Size(self,Size):
		self.add_query_param('Size',Size)

	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)

	def get_StartTimeStamp(self):
		return self.get_query_params().get('StartTimeStamp')

	def set_StartTimeStamp(self,StartTimeStamp):
		self.add_query_param('StartTimeStamp',StartTimeStamp)

	def get_EndTimeStamp(self):
		return self.get_query_params().get('EndTimeStamp')

	def set_EndTimeStamp(self,EndTimeStamp):
		self.add_query_param('EndTimeStamp',EndTimeStamp)