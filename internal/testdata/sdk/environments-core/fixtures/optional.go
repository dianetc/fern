// This file was auto-generated by Fern from our API Definition.

package api

import (
	core "github.com/fern-api/fern-go/internal/testdata/sdk/environments-core/fixtures/core"
)

// Optional initializes an optional field.
func Optional[T any](value T) *core.Optional[T] {
	return &core.Optional[T]{
		Value: value,
	}
}

// Null initializes an optional field that will be sent as
// an explicit null value.
func Null[T any]() *core.Optional[T] {
	return &core.Optional[T]{
		Null: true,
	}
}
