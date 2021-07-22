/*
Copyright 2021 Cortex Labs, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package status

type Status struct {
	APIName       string `json:"api_name"`
	APIID         string `json:"api_id"`
	Code          Code   `json:"status_code"`
	ReplicaCounts `json:"replica_counts"`
}

type ReplicaCounts struct {
	Updated   SubReplicaCounts `json:"updated,omitempty"`
	Stale     SubReplicaCounts `json:"stale,omitempty"`
	Requested int32            `json:"requested,omitempty"`
}

type SubReplicaCounts struct {
	Pending      int32 `json:"pending,omitempty"`
	Initializing int32 `json:"initializing,omitempty"`
	Ready        int32 `json:"ready"`
	NotReady     int32 `json:"not_ready,omitempty"`
	ErrImagePull int32 `json:"err_image_pull,omitempty"`
	Terminating  int32 `json:"terminating,omitempty"`
	Failed       int32 `json:"failed,omitempty"`
	Killed       int32 `json:"killed,omitempty"`
	KilledOOM    int32 `json:"killed_oom,omitempty"`
	Stalled      int32 `json:"stalled,omitempty"` // pending for a long time
	Unknown      int32 `json:"unknown,omitempty"`
}

// Worker counts don't have as many failure variations because Jobs clean up dead pods, so counting different failure scenarios isn't interesting
type WorkerCounts struct {
	Pending      int32 `json:"pending,omitempty"`
	Initializing int32 `json:"initializing,omitempty"`
	Running      int32 `json:"running,omitempty"`
	Succeeded    int32 `json:"succeeded,omitempty"`
	Failed       int32 `json:"failed,omitempty"`
	Stalled      int32 `json:"stalled,omitempty"` // pending for a long time
	Unknown      int32 `json:"unknown,omitempty"`
}

func (status *Status) Message() string {
	return status.Code.Message()
}

func (src *SubReplicaCounts) TotalFailed() int32 {
	return src.Failed + src.ErrImagePull + src.Killed + src.KilledOOM + src.Stalled
}
