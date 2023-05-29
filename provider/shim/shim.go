package shim

import (
	"github.com/hashicorp/terraform-plugin-framework/provider"
	p "github.com/fluxcd/terraform-provider-flux/internal/provider"
)

func NewProvider() provider.Provider {
	return p.New("0.24.0")()
}