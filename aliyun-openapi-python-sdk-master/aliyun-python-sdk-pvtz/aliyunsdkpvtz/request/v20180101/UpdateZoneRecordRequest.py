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
class UpdateZoneRecordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'pvtz', '2018-01-01', 'UpdateZoneRecord','pvtz')

	def get_Rr(self):
		return self.get_query_params().get('Rr')

	def set_Rr(self,Rr):
		self.add_query_param('Rr',Rr)

	def get_RecordId(self):
		return self.get_query_params().get('RecordId')

	def set_RecordId(self,RecordId):
		self.add_query_param('RecordId',RecordId)

	def get_UserClientIp(self):
		return self.get_query_params().get('UserClientIp')

	def set_UserClientIp(self,UserClientIp):
		self.add_query_param('UserClientIp',UserClientIp)

	def get_Lang(self):
		return self.get_query_params().get('Lang')

	def set_Lang(self,Lang):
		self.add_query_param('Lang',Lang)

	def get_Type(self):
		return self.get_query_params().get('Type')

	def set_Type(self,Type):
		self.add_query_param('Type',Type)

	def get_Priority(self):
		return self.get_query_params().get('Priority')

	def set_Priority(self,Priority):
		self.add_query_param('Priority',Priority)

	def get_Ttl(self):
		return self.get_query_params().get('Ttl')

	def set_Ttl(self,Ttl):
		self.add_query_param('Ttl',Ttl)

	def get_Value(self):
		return self.get_query_params().get('Value')

	def set_Value(self,Value):
		self.add_query_param('Value',Value)